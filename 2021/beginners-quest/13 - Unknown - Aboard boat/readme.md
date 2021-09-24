> Reference: https://github.com/Dvd848/CTFs/blob/master/2021_GoogleCTF_BQ/13_Unknown_-_Aboard_boat.md

1. `tshark -qz io,phs -r '../resources/httponly.pcap'`

1. `tshark -r '../resources/httponly.pcap' -qz follow,tcp,ascii,1`

1. `tshark -r '../resources/httponly.pcap' -qz follow,tcp,ascii,3`

1. `node decrypt.js`

1. `tshark -r "../resources/httponly.pcap" -o "tcp.desegment_tcp_streams: TRUE" -o "tcp.no_subdissector_on_error: FALSE" --export-objects "http,exported_objects"`

1. `unzip -P BossToldMeToSetABetterPasswordSoThisWillHaveToDo1234 exported_objects/flag.zip`

1. `cat flag.txt`

> CTF{PleaseAssumeThisIsSomeSecretStuffThankYou}
