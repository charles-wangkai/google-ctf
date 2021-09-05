import { decode } from "base65536";
import { readFileSync, writeFileSync } from "fs";

writeFileSync(
  "base_decoded.txt",
  decode(
    readFileSync(
      "../resources/306a5e3c0faa213b4b3348366938020f90d38a41ae136a46547553fb3d6961c4bf598da6378092b4afd60f60a2510898c59d1a091961f0729c4839b1a6266a8f/chall.txt",
      "utf-8"
    )
  )
);
