class BaobabTree {
    constructor(season) {
        this.season = season;
        this.fruit = null;
    }

    getSeasonalFruit() {
        switch (this.season) {
            case 'Spring':
                this.fruit = new Fruit('Magic Apple', 'Healing');
                break;
            case 'Summer':
                this.fruit = new Fruit('Star Fruit','Speed');
                break;
            case 'Autumn':
                this.fruit = new Fruit('Moon Berry', 'Wisdom');
                break;
            case 'Winter':
                this.fruit = new Fruit('Ice Grape', 'Cold Resistance');
                break;
            default:
                console.log('Invalid season');
        }
        return this.fruit;
    }

    logEffects() {
        if (this.fruit) {
            console.log(`Consuming ${this.fruit.type} grants you ${this.fruit.powers}`);
        } else {
            console.log('No fruit for this season.');
        }
    }
}

class Fruit {
    constructor(type, powers) {
        this.type = type;
        this.powers = powers;
    }
}

// Usage example
const myTree = new BaobabTree('Spring');

console.log(myTree.getSeasonalFruit().type); // Output: Magic Apple
myTree.logEffects(); // Output: Consuming Magic Apple grants you Healing, Strength
