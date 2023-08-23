import {Link} from 'react-router-dom'

function Navbar() {
    return (
        <nav className="navbar">
            <h1><Link to="/">Food App</Link></h1>
            <div className="links">
                <Link to="/">Home</Link>
                <Link to="/Camera">Take Photo</Link>
            </div>
        </nav>
    );
}



export default Navbar;