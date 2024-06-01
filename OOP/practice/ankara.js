class EnvironmentalMoodData {
    constructor() {
        this.temperature = null;
        this.mood = null;
    }

    update(tempValue, moodState) {
        this.temperature = tempValue;
        this.mood = moodState;
    }

    getTemperature() {
        return this.temperature;
    }

    getMood() {
        return this.mood;
    }

    classifyTemperature() {
        if (this.temperature < 10) {
            return "cold";
        } else if (10 <= this.temperature && this.temperature <= 30) {
            return "neutral";
        } else {
            return "hot";
        }
    }
}

class FabricDesign {
    constructor(colorScheme, patternType) {
        this.colorScheme = colorScheme;
        this.patternType = patternType;
    }
}

class Predictor {
    constructor() {
        this.environmentalData = new EnvironmentalMoodData();
    }

    updateEnvironmentalData(tempValue, moodState) {
        this.environmentalData.update(tempValue, moodState);
    }

    predictNextDesign() {
        const temperatureCategory = this.environmentalData.classifyTemperature();
        if (temperatureCategory === "hot" && this.environmentalData.getMood() === "happy") {
            return new FabricDesign("Bright", "Stripes");
        } else if (temperatureCategory === "hot" && this.environmentalData.getMood() === "sad") {
            return new FabricDesign("Dark", "Floral");
        } else if (temperatureCategory === "neutral") {
            return new FabricDesign("Neutral", "Solid");
        } else {
            return new FabricDesign("Warm", "Plaid"); // Default for cold temperatures
        }
    }
}
