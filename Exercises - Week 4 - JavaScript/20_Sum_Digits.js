function sumDigits(num) {
  let sum = 0;

  const digits = num.toString().split("");

  for (let i = 0; i < digits.length; i++) {
    sum += parseInt(digits[i], 10);
  }

  return sum;
}
