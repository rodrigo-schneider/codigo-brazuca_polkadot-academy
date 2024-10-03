function isPalindrome(str) {
  const cleanedStr = str.replace(/\s+/g, "").toLowerCase();

  const reversedStr = cleanedStr.split("").reverse().join("");

  return cleanedStr === reversedStr;
}
