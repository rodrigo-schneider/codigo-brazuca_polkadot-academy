function fibonacciSequence(n) {
  const sequence = [0, 1];

  for (let i = 2; i < n; i++) {
    const nextTerm = sequence[i - 1] + sequence[i - 2];
    sequence.push(nextTerm);
  }

  return sequence;
}

const fibonacciTenTerms = fibonacciSequence(10);
console.log(fibonacciTenTerms);
