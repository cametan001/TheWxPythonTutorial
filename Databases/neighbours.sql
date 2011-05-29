BEGIN TRANSACTION;
CREATE TABLE neighbours(name text, age numeric, remark text);
INSERT INTO "neighbours" VALUES('sandy',7,'stubborn');
INSERT INTO "neighbours" VALUES('jane',18,'beautiful');
INSERT INTO "neighbours" VALUES('mark',28,'lazy');
INSERT INTO "neighbours" VALUES('steven',34,'friendly');
INSERT INTO "neighbours" VALUES('alice',17,'slick');
INSERT INTO "neighbours" VALUES('tom',25,'clever');
INSERT INTO "neighbours" VALUES('jack',89,'wise');
INSERT INTO "neighbours" VALUES('lucy',18,'cute');
COMMIT;

