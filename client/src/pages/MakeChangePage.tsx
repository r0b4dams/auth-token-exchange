import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { useFusionAuth } from "@fusionauth/react-sdk";

import { USDollars } from "../utils";

interface Change {
  [key: string]: number;
  total: number;
  quarters: number;
  dimes: number;
  nickels: number;
  pennies: number;
}

export const MakeChangePage = () => {
  const navigate = useNavigate();
  const { userInfo } = useFusionAuth();
  const isLoggedIn = !!userInfo;

  const [amount, setAmount] = useState(0);
  const [change, setChange] = useState<Change | null>(null);

  useEffect(() => {
    if (!isLoggedIn) {
      navigate("/");
    }
  }, [isLoggedIn, navigate]);

  const makeChange: React.FormEventHandler<HTMLFormElement> = (e) => {
    e.stopPropagation();
    e.preventDefault();

    const total = amount ?? 0;

    if (total === 0) {
      return;
    }

    let pennies = Math.trunc(total * 100);
    console.log(pennies);

    const quarters = Math.floor(pennies / 25);
    pennies -= quarters * 25;

    const dimes = Math.floor(pennies / 10);
    pennies -= dimes * 10;

    const nickels = Math.floor(pennies / 5);
    pennies -= nickels * 5;

    setChange({ total, quarters, dimes, nickels, pennies });
  };

  const renderChange = () => {
    if (!change) {
      return null;
    }
    return Object.entries<number>(change)
      .filter(([key]) => key !== "total")
      .map(([coin, num]) => (
        <p key={coin}>
          {coin[0].toUpperCase() + coin.substring(1)} {num}
        </p>
      ));
  };

  const handleFocus: React.FocusEventHandler<HTMLInputElement> = (e) => {
    e.target.select();
  };

  const handleInput: React.ChangeEventHandler<HTMLInputElement> = (e) => {
    setAmount(parseFloat(e.target.value));
  };

  if (!isLoggedIn) {
    return null;
  }

  return (
    <div className="app-container change-container">
      <h3>We Make Change</h3>

      <form onSubmit={makeChange}>
        <div className="h-row">
          <div className="change-label">Amount in USD: $</div>
          <input
            className="change-input"
            name="amount"
            value={amount}
            onFocus={handleFocus}
            onChange={handleInput}
            type="number"
            step=".01"
            min={0}
          />
          <input className="change-submit" type="submit" value="Make Change" />
        </div>
      </form>

      {change && (
        <div className="change-message">
          <p>We can make change for {USDollars.format(change.total)} with:</p>
          <div style={{ paddingLeft: 25 }}>{renderChange()}</div>
        </div>
      )}
    </div>
  );
};
