import {useState} from 'react'

function Nutrition({food}) {
    const [foodData, setFoodData] = useState(null)

    const urlParams = {
        api_key: "DpfO2fJSAweQgObaZsjxtDje8y0DfWMdh2bkNzRl",
        query: food,
        dataType: ["Survey (FNDDS)"],
        pageSize: 5
    }

    const url = `https://api.nal.usda.gov/fdc/v1/foods/search?api_key=${encodeURIComponent(params.api_key)}&query=${encodeURIComponent(params.query)}&dataType=${encodeURIComponent(params.dataType)}&pageSize=${encodeURIComponent(params.pageSize)}`

    useEffect(() => {
        fetch(url)
        .then(res => res.json())
        .then(data => {setFoodData(data)})
    }, []);


    return (
        <div className="nutrition">
            <h2>Nutrition Facts</h2>
            {foodData && foodData.foods && foodData.foods.length > 0 && 
            <div>{JSON.stringify(foodData.foods[0].foodNutrients)}</div>}
        </div>
    );
}

export default Nutrition;