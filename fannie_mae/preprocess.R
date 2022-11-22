# see https://github.com/NVIDIA/fsi-samples/tree/main/credit_default_risk
# see https://docs.rapids.ai/datasets/mortgage-data
# see our Nvidia blog post https://developer.nvidia.com/blog/best-practices-explainable-ai-powered-by-synthetic-data/


# wget http://rapidsai-data.s3-website.us-east-2.amazonaws.com/notebook-mortgage-data/mortgage_2000-2016.tgz
# tar xzvf mortgage_2000-2016.tgz
# cat Performance_2009Q1.txt_1 > Performance_2009Q1.txt_0
# cat Performance_2009Q2.txt_1 > Performance_2009Q2.txt_0
# cat Performance_2009Q3.txt_1 > Performance_2009Q3.txt_0
# cat Performance_2010Q4.txt_1 > Performance_2010Q4.txt_0
# cat Performance_2011Q4.txt_1 > Performance_2011Q4.txt_0
# cat Performance_2012Q1.txt_1 > Performance_2012Q1.txt_0
# cat Performance_2012Q2.txt_1 > Performance_2012Q2.txt_0
# cat Performance_2012Q3.txt_1 > Performance_2012Q3.txt_0
# cat Performance_2012Q4.txt_1 > Performance_2012Q4.txt_0


library(data.table)
library(lubridate)

fns <- list.files('acq', full.names=T)

lapply(fns, function(fn_a) {
  
  quarter <- substr(fn, nchar(fn) - 9, nchar(fn)-4)
  fn_a <- fn
  fn_p <- paste0('perf/Performance_', quarter, '.txt')
  
  a <- fread(fn_a, sep='|', header=F)
  setnames(a, c('LoanID', 'Channel', 'SellerName', 'OrInterestRate', 'OrUnpaidPrinc', 'OrLoanTerm',
                'OrDate', 'FirstPayment', 'OrLTV', 'OrCLTV', 'NumBorrow', 'DTIRat', 'CreditScore',
                'FTHomeBuyer', 'LoanPurpose', 'PropertyType', 'NumUnits', 'OccStatus', 'PropertyState',
                'Zip', 'MortInsPerc', 'ProductType', 'CoCreditScore', 'Extra', 'MortInsType', 'RelMortInd'))
  a[, Zip := as.character(Zip)]
  a[, LoanID := as.character(LoanID)]

  p = fread(fn_p, sep='|', header=F, select=c(1, 11), col.names = c('LoanID', 'CLDS'), colClasses = 'character')
  p = p[CLDS== '4']

  df = merge(a, p, all=T, by='LoanID')
  df[, Default := 0]
  df[CLDS==4, Default := 1]
  df[, CLDS := NULL]
  df[, c('LoanID', 'OrDate','OrLTV','MortInsPerc','RelMortInd','FirstPayment') := NULL]
  setcolorder(df, 'Default')
  
  fwrite(df, paste0(quarter, '.csv'))
  
})
