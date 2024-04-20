import { Outlet } from "react-router-dom";
import { Footer, Header } from "./components";

export const AppLayout: React.FC = (): JSX.Element => {
  return (
    <>
      <Header />
      <main className="flex justify-center items-center">
        <Outlet />
      </main>
      <Footer />
    </>
  );
};