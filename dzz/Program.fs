// Абстрактный класс для приготовления кофе
[<AbstractClass>]
type CoffeeBrewer() =
    abstract member Brew: unit -> string

// Конкретные реализации приготовления кофе
type EspressoBrewer() =
    inherit CoffeeBrewer()
    override this.Brew() = "Приготовлен эспрессо: насыщенный и крепкий"

type CappuccinoBrewer() =
    inherit CoffeeBrewer()
    override this.Brew() = "Приготовлен капучино: с молочной пенкой"

type LatteBrewer() =
    inherit CoffeeBrewer()
    override this.Brew() = "Приготовлен латте: много молока, мягкий вкус"

type AmericanoBrewer() =
    inherit CoffeeBrewer()
    override this.Brew() = "Приготовлен американо: эспрессо с водой"

// Абстрактный класс кофемашины
[<AbstractClass>]
type CoffeeMachine() =
    abstract member MakeCoffee: unit -> string

// Конкретная кофемашина с внедрением зависимости
type AutomaticCoffeeMachine(brewer: CoffeeBrewer) =
    inherit CoffeeMachine()
    
    override this.MakeCoffee() =
        $"Автоматическая кофемашина: {brewer.Brew()}"

// Другой тип кофемашины
type ManualCoffeeMachine(brewer: CoffeeBrewer) =
    inherit CoffeeMachine()
    
    override this.MakeCoffee() =
        $"Ручная кофемашина (бариста): {brewer.Brew()}"

// Сервис для приготовления кофе
type CoffeeService(machine: CoffeeMachine) =
    member this.ServeCoffee() =
        machine.MakeCoffee()

// Фабрика для создания различных типов кофе
module CoffeeFactory =
    let createEspressoMachine() =
        AutomaticCoffeeMachine(EspressoBrewer())
    
    let createCappuccinoMachine() =
        AutomaticCoffeeMachine(CappuccinoBrewer())
    
    let createLatteMachine() =
        ManualCoffeeMachine(LatteBrewer())
    
    let createAmericanoMachine() =
        ManualCoffeeMachine(AmericanoBrewer())

// Пример использования с внедрением зависимостей
module Program =
    // Функция для демонстрации разных конфигураций
    let demonstrateCoffeePreparation() =
        printfn "=== Приготовление кофе с DI ==="
        
        // Создаем различные конфигурации кофемашин
        let espressoService = CoffeeService(CoffeeFactory.createEspressoMachine())
        let cappuccinoService = CoffeeService(CoffeeFactory.createCappuccinoMachine())
        let latteService = CoffeeService(CoffeeFactory.createLatteMachine())
        let americanoService = CoffeeService(CoffeeFactory.createAmericanoMachine())
        
        // Используем сервисы
        printfn "%s" (espressoService.ServeCoffee())
        printfn "%s" (cappuccinoService.ServeCoffee())
        printfn "%s" (latteService.ServeCoffee())
        printfn "%s" (americanoService.ServeCoffee())
        
        // Демонстрация гибкости: можно легко заменить тип приготовления
        printfn "\n=== Замена типа приготовления ==="
        let customMachine = ManualCoffeeMachine(EspressoBrewer())
        let customService = CoffeeService(customMachine)
        printfn "%s" (customService.ServeCoffee())
    
    [<EntryPoint>]
    let main argv =
        demonstrateCoffeePreparation()
        0