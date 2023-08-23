import { useNavigate } from "react-router-dom";

function Home() {
    const navigate = useNavigate();

    const handleClick = () => {
        navigate("/camera");
    }

    return (
        <div className="Home">
            <h2>Welcome to our computer vision nutrition website!</h2>
            <button onClick={handleClick}>Take a photo of a food item!</button>
        </div>
    );
}

export default Home;