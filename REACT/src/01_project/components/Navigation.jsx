import { useState } from "react";
import myimg from "../public/sneakers.png";
import "./Navigation.css";

export default function Navigation() {
  const [open, setOpen] = useState(false);

  return (
    <nav className="nav">
      <img src={myimg} alt="logo" className="nav-logo" />

      <button
        className="hamburger"
        aria-expanded={open}
        aria-label="Toggle menu"
        onClick={() => setOpen(!open)}
      >
        ☰
      </button>

      <ul className={`nav-list ${open ? "open" : ""}`}>
        <li>Home</li>
        <li>Contact</li>
        <li>About</li>
        <li>Other</li>
      </ul>

      <button className="login-btn">Login</button>
    </nav>
  );
}
