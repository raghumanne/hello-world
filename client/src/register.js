import React from "react"

function Register() {
    return(
        <div className="login-body">
			<form className="form-container">
			  <div className="container">
			    <label className="uname"><b>Username</b></label>
			    <input type="text"  className="usname" placeholder="Enter Username" name="uname" required />
			    <label className="pwd"><b>Password</b></label>
			    <input type="password" className="psw"  placeholder="Enter Password" name="psw" required />
			    <div className="load-div"><button type="submit" className="submitbtn">Login<img className="login-load" alt="logo" /></button></div>   
			  </div>
			</form>
     		 </div>
    )
}

export default Register