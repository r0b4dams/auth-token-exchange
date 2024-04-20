import { useFusionAuth } from "@fusionauth/react-sdk";
import { Button } from "./Button";

export const Header: React.FC = (): JSX.Element => {
  const { isAuthenticated, logout } = useFusionAuth();

  return (
    <header className="h-[10vh] flex justify-end items-center px-5">
      {isAuthenticated && (
        <div>
          <Button onClick={() => logout()}>Logout</Button>
        </div>
      )}
    </header>
  );
};
