import './Header.css'

function Header() {
    return <header>
            <h1>Smart Card</h1>
            <nav>
                <ul>
                    <li>
                        <a className="nav-link active" aria-current="page" href="#">HOME</a>
                    </li>
                    <li>
                        <a className="nav-link" href="#">CONTACT US</a>
                    </li>
                </ul>
            </nav>
        </header>
}



export default Header;