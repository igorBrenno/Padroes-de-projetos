# Abstract Factory Pattern 🏗️

## Descrição
O **Abstract Factory** é um padrão de projeto criacional que permite produzir famílias de objetos relacionados (ou dependentes) sem especificar suas classes concretas.

Enquanto o *Factory Method* cria apenas um produto, o *Abstract Factory* cria um "kit" de produtos que devem ser usados juntos.

## 🧱 Componentes
1.  **Abstract Factory**: Interface que declara métodos de criação para cada produto abstrato.
2.  **Concrete Factories**: Implementam os métodos criando produtos de uma variante específica (ex: WindowsFactory).
3.  **Abstract Products**: Interfaces para o conjunto de produtos distintos (ex: Botão, Checkbox).
4.  **Concrete Products**: Implementações específicas dos produtos para cada variante.

## ✅ Vantagens
- **Consistência**: Garante que os produtos que você obtém de uma fábrica sejam compatíveis entre si.
- **Isolamento**: O código cliente não se acopla às implementações concretas das variantes.
- **Princípio da Responsabilidade Única**: O código de criação de produtos é extraído para um único lugar.

## ⚠️ Desvantagens
- **Complexidade**: O código pode se tornar complicado, pois exige muitas interfaces e classes novas.
- **Dificuldade de Extensão**: Adicionar um novo tipo de produto (ex: uma "Barra de Rolagem") exige alterar a interface da fábrica e todas as suas implementações.

---