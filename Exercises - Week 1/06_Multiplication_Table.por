programa {
  funcao inicio() {

    inteiro numero

    escreva("Digite o n�mero para saber a tabuada: ")
    leia(numero)

    para(inteiro i = 1; i <= 10; i++) {
      escreva(numero, " x ", i, " = ", numero * i, "\n")
    }
    
  }
}
