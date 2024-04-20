import { Button } from "../components/Button";
import { Navigate } from "react-router-dom";
import { useFusionAuth } from "@fusionauth/react-sdk";

export const Home: React.FC = (): JSX.Element => {
  const { isAuthenticated, login, register } = useFusionAuth();

  if (isAuthenticated) {
    return <Navigate to="/profile" />;
  }

  return (
    <div className="flex flex-col justify-center items-center space-y-10">
      <Button onClick={() => login()}>Login</Button>
      <Button onClick={() => register()}>Signup</Button>
    </div>
  );
};
