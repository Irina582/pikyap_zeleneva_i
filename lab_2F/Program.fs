open System

type GeometricFigure =
    | Rectangle of width: float * height: float
    | Square of side: float
    | Circle of radius: float


let S figure =
    match figure with
    | Rectangle(w, h) -> w * h
    | Square(s) -> s * s
    | Circle(r) -> Math.PI * r * r

let printFigure figure =
    let area = S figure
    match figure with
    | Rectangle(w, h) -> 
        printfn "Ширина прямоугольника = %.2f, высота прямоугольника = %.2f, площадь прямоугольника = %.2f" w h area
    | Square(s) -> 
        printfn "Сторона квадрата = %.2f, площадь квадрата= %.2f" s area
    | Circle(r) -> 
        printfn "Радиус круга= %.2f, площадь круга = %.2f" r area

[<EntryPoint>]
let main argv =
    let rect = Rectangle(9.0, 2.0)
    let square = Square(7.0)
    let circle = Circle(5.0)

    printFigure rect
    printFigure square
    printFigure circle

    0