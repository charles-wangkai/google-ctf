function decryptWithMilitaryGradeEncryption(hexstr) {
  const len = hexstr.length;

  const key = Uint8Array.from([11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 202]);
  const keylen = key.length;

  const arr = [];

  for (let i = 0; i < len; i += 2) {
    const byte = parseInt(hexstr.substring(i, i + 2), 16);
    arr.push(byte ^ key[(i >> 1) % keylen]);
  }

  const decoder = new TextDecoder();
  return decoder.decode(Uint8Array.from(arr));
}

console.log(
  decryptWithMilitaryGradeEncryption(
    "717f510b44623d391016bd6464450c5e316d1a0c16b95f794d487a2719373000be4a54445843273f080216b97c795348642d19300a169d627a4d645634280c0c21a53a241218"
  )
); // zip's password is BossToldMeToSetABetterPasswordSoThisWillHaveToDo1234
console.log(decryptWithMilitaryGradeEncryption("72734044")); // yeah
