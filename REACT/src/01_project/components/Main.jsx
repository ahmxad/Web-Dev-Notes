import "./Main.css";
import myimg from "../public/sneakers.png";
export default function Main() {
  return (
    <main>
      <div className="con">
        <div className="logo">  
        <img src={myimg} alt="logo" />
        </div>
        <div className="texbtn">
          <div className="text">
            <h1>Your new shoe store</h1>
            <p>This is the best shoe store ever</p>
          </div>
          <div className="btn">
            <button>Shop now</button>
            <button>More...</button>
          </div>
        </div>
        <div className="img">
          <img src={myimg} alt="shoe" />
        </div>
      </div>
    </main>
  );
}
