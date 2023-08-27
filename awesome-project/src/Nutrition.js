import {useState, useEffect} from 'react'

function Nutrition({food}) {
    const [foodData, setFoodData] = useState(null);
    const [nutrients, setNutrients] = useState(
    {
        1008: null,
        1004: null,
        1003: null,
        1005: null,
        2000: null,
        1079: null
    });

    const params = {
        api_key: "DpfO2fJSAweQgObaZsjxtDje8y0DfWMdh2bkNzRl",
        query: food,
        dataType: ["Survey (FNDDS)"],
        pageSize: 5
    }

    const desiredNutrients = {
        1008:"Calories",
        1004:"Total Fat",
        1003:"Protein",
        1005:"Total Carbohydrate",
        2000:"Total Sugars",
        1079:"Dietary Fiber"
    }

    const url = `https://api.nal.usda.gov/fdc/v1/foods/search?api_key=${encodeURIComponent(params.api_key)}&query=${encodeURIComponent(params.query)}&dataType=${encodeURIComponent(params.dataType)}&pageSize=${encodeURIComponent(params.pageSize)}`

    useEffect(() => {
        fetch(url)
        .then(res => res.json())
        .then(data => {setFoodData(data.foods[0])})
    }, [url]);

    const getDesiredNutrients = (nutrients) => {
        return nutrients.filter(
            n => desiredNutrients.hasOwnProperty(n.nutrientId)
        );
    }

    return (
        <div className="nutrition">
            <h2>{food.toUpperCase()}<br /> Nutrition Facts (for 100 g)</h2>
            <ul>
                {foodData &&
                getDesiredNutrients(foodData.foodNutrients).map((n) => (
                    <li key={n.nutrientId}>{desiredNutrients[n.nutrientId]}: {n.value} {n.unitName.toLowerCase()}</li>
                ))}
            </ul>
            {foodData && console.log(foodData)}
        </div>
    );
}

export default Nutrition;