import './Header.css'
import image from '../assets/IMG_4.JPG'

function Header() {
    return <header>
            <h2>Smart Card</h2>
            <div className='headerRight'>
                <nav>
                    <ul>
                        <li>HOME</li>
                        <li>CONTACT US</li>
                    </ul>
                </nav>
                <div className='profile'>
                    <img src={image}/> 
                </div>
            </div>
        </header>
}



export default Header;