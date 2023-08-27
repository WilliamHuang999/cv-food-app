import { useState } from "react";
import { useNavigate } from "react-router-dom";

function AddFood({nutrientData}) {
    const navigate = useNavigate();
    const [grams, setGrams] = useState(0)

    const handleCancel = () => {
        navigate("/")
    }

    const handleAdd = () => {
        // f
    }

    return (
        <>
            <Nutrition food="cheddar cheese"/>
            <label htmlFor="grams">Enter the food amount in grams:</label>
            <input type="number" id="grams" required placeholder="Enter grams" size="10"
            onChange={(e) => setGrams(e.target.value)}/>

            <button onClick={handleCancel}>Cancel</button>
            <button>Add</button>
        </>
    );
}

export default AddFood;