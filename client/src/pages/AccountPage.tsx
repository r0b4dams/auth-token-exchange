import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { useFusionAuth } from "@fusionauth/react-sdk";

import { USDollars } from "../utils";

export const AccountPage = () => {
  const [balance] = useState(
    USDollars.format(Math.ceil(Math.random() * 100000) / 100)
  );
  const navigate = useNavigate();
  const { userInfo, isFetchingUserInfo } = useFusionAuth();
  const isLoggedIn = !!userInfo;

  useEffect(() => {
    if (!isLoggedIn) {
      navigate("/");
    }
  }, [isLoggedIn, navigate]);

  if (!isLoggedIn || isFetchingUserInfo) {
    return null;
  }

  return (
    <div className="column-container">
      <div className="app-container">
        <h3>Your balance</h3>
        <div className="balance">{balance}</div>
      </div>
    </div>
  );
};
