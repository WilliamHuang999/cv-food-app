

function FoodList({foods}) {
    return (
        <div className="food-list">
            <ul>
                {foods.map((f) => (
                    <li><a href={`/nutrition/${f}`}>{f}</a></li>
                ))}
            </ul>
        </div>
    );
}

export default FoodList;