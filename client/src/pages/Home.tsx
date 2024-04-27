import { Button } from "../components/Button";
import { Navigate } from "react-router-dom";
import { useFusionAuth } from "@fusionauth/react-sdk";

export const Home: React.FC = (): JSX.Element => {
  const { isLoggedIn, startLogin, startRegister } = useFusionAuth();

  if (isLoggedIn) {
    return <Navigate to="/profile" />;
  }

  return (
    <div className="flex flex-col justify-center items-center space-y-10">
      <Button onClick={() => startLogin()}>Login</Button>
      <Button onClick={() => startRegister()}>Signup</Button>
    </div>
  );
};
