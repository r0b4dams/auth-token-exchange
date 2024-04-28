import { useFusionAuth } from "@fusionauth/react-sdk";
import { NavLink } from "react-router-dom";

export const MenuBar = () => {
  const { userInfo } = useFusionAuth();
  const isLoggedIn = !!userInfo;

  return (
    <div id="menu-bar" className="menu-bar">
      {isLoggedIn ? (
        <>
          <NavLink to="/make-change" className="menu-link">
            Make Change
          </NavLink>

          <NavLink to="/account" className="menu-link">
            Account
          </NavLink>

          <NavLink to="/profile" className="menu-link">
            Profile
          </NavLink>
        </>
      ) : (
        <>
          <button className="menu-link">About</button>
          <button className="menu-link">Services</button>
          <button className="menu-link">Products</button>
          <button
            className="menu-link"
            style={{ textDecorationLine: "underline" }}
          >
            Home
          </button>
        </>
      )}
    </div>
  );
};
