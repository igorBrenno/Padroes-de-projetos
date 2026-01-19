# Padrão de Projeto: Mediator (Mediador)

## 📌 Objetivo
O **Mediator** é um padrão de projeto comportamental que permite reduzir as dependências diretas entre objetos. Ele restringe a comunicação direta entre os objetos e os força a colaborar apenas através de um objeto mediador.



---

## 🧩 Como funciona?
Imagine uma **Torre de Controle de Tráfego Aéreo**. Os pilotos de aviões que se aproximam ou partem do aeroporto não se comunicam diretamente entre si. Se o fizessem, teriam que saber a posição e intenção de todos os outros aviões ao mesmo tempo, criando uma teia de comunicação impossível de gerenciar.

Em vez disso, cada piloto fala com a **Torre**. A Torre sabe onde todos os aviões estão e coordena quem deve pousar ou esperar.

### Componentes:
* **Mediator (Interface)**: Define a interface para comunicação com os componentes.
* **Concrete Mediator**: Implementa o comportamento cooperativo coordenando os componentes. Ele conhece e mantém os componentes.
* **Colleagues (Componentes)**: Cada classe componente conhece apenas o seu Mediador, comunicando-se com ele em vez de falar com outros componentes.

## ✅ Vantagens
* **Single Responsibility Principle**: Você pode extrair as comunicações entre vários componentes para um único lugar.
* **Open/Closed Principle**: Você pode introduzir novos mediadores sem ter que mudar os componentes reais.
* **Redução de Acoplamento**: Facilita a manutenção, pois as dependências entre componentes são eliminadas.

## ❌ Desvantagens
* **Objeto Deus (God Object)**: Com o tempo, um mediador pode evoluir para um objeto excessivamente complexo que é difícil de manter, pois ele centraliza toda a lógica de interação.