
CREATE TABLE district (
	district_id int8 NOT NULL,
	"A2" text NULL,
	"A3" text NULL,
	"A4" int8 NULL,
	"A5" int8 NULL,
	"A6" int8 NULL,
	"A7" int8 NULL,
	"A8" int8 NULL,
	"A9" int8 NULL,
	"A10" float8 NULL,
	"A11" int8 NULL,
	"A12" text NULL,
	"A13" float8 NULL,
	"A14" int8 NULL,
	"A15" text NULL,
	"A16" int8 NULL,
	CONSTRAINT district_pkey PRIMARY KEY (district_id)
);

CREATE TABLE account (
	account_id int8 NOT NULL,
	district_id int8 NULL,
	frequency text NULL,
	"date" timestamp NULL,
	CONSTRAINT account_pkey PRIMARY KEY (account_id),
	CONSTRAINT fk_district FOREIGN KEY (district_id) REFERENCES district(district_id)
);

CREATE TABLE client (
	client_id int8 NOT NULL,
	birth_number int8 NULL,
	district_id int8 NULL,
	CONSTRAINT client_pkey PRIMARY KEY (client_id),
	CONSTRAINT fk_district FOREIGN KEY (district_id) REFERENCES district(district_id)
);

CREATE TABLE disp (
	disp_id int8 NOT NULL,
	client_id int8 NULL,
	account_id int8 NULL,
	"type" text NULL,
	CONSTRAINT disp_pkey PRIMARY KEY (disp_id),
	CONSTRAINT fk_account FOREIGN KEY (account_id) REFERENCES account(account_id),
	CONSTRAINT fk_client FOREIGN KEY (client_id) REFERENCES client(client_id)
);

CREATE TABLE loan (
	loan_id int8 NOT NULL,
	account_id int8 NULL,
	"date" timestamp NULL,
	amount int8 NULL,
	duration int8 NULL,
	payments int8 NULL,
	status text NULL,
	CONSTRAINT loan_pkey PRIMARY KEY (loan_id),
	CONSTRAINT fk_account FOREIGN KEY (account_id) REFERENCES account(account_id)
);

CREATE TABLE "order" (
	order_id int8 NOT NULL,
	account_id int8 NULL,
	bank_to text NULL,
	account_to int8 NULL,
	amount float8 NULL,
	k_symbol text NULL,
	CONSTRAINT order_pkey PRIMARY KEY (order_id),
	CONSTRAINT fk_account FOREIGN KEY (account_id) REFERENCES account(account_id)
);

CREATE TABLE trans (
	trans_id int8 NOT NULL,
	account_id int8 NULL,
	"date" timestamp NULL,
	"type" text NULL,
	operation text NULL,
	amount float8 NULL,
	balance float8 NULL,
	k_symbol text NULL,
	bank text NULL,
	account int8 NULL,
	CONSTRAINT trans_pkey PRIMARY KEY (trans_id),
	CONSTRAINT fk_account FOREIGN KEY (account_id) REFERENCES account(account_id)
);

CREATE TABLE card (
	card_id int8 NOT NULL,
	disp_id int8 NULL,
	"type" text NULL,
	issued timestamp NULL,
	CONSTRAINT card_pkey PRIMARY KEY (card_id),
	CONSTRAINT fk_disp FOREIGN KEY (disp_id) REFERENCES disp(disp_id)
);
