# Prototype Pattern 🧬

## Descrição
O **Prototype** permite a criação de novos objetos a partir de um modelo original (protótipo). O objetivo é copiar um objeto existente em vez de criar um novo do zero, facilitando a gestão de estados complexos.

## 🛠 Como funciona?
A classe que será clonada implementa um método `clonar()`. No Python, utilizamos frequentemente o módulo nativo `copy` para realizar **Shallow Copies** (cópias rasas) ou **Deep Copies** (cópias profundas).

## ✅ Vantagens
- **Independência de Classes Concretas:** O cliente não precisa conhecer as classes dos objetos que está clonando.
- **Eficiência:** Reduz o custo de inicialização de objetos complexos.
- **Flexibilidade:** Permite adicionar ou remover protótipos em tempo de execução.

## ⚠️ Desvantagens
- **Referências Circulares:** Clonar objetos complexos que possuem referências circulares pode ser muito difícil.
- **Deep Copy Necessário:** Se o objeto tiver listas ou outros objetos internos, uma cópia simples apenas copiará os endereços de memória, exigindo o uso de `deepcopy`.

---