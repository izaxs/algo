// Mapped Types
// https://www.typescriptlang.org/docs/handbook/2/mapped-types.html
type Fruit = 'apple' | 'banana' | 'orange';
type FruitCount = { 
    [K in Fruit]: number 
};
const fruitCount: FruitCount = {
    apple: 1,
    banana: 2,
    orange: 3,
};

type Person = {
    name: string;
    age: number;
}
type Gauge = {
    [key in keyof Person]: number
}

const myGauge: Gauge = {
    name: 1,
    age: 2,
};
