import { useEffect, useState } from "react";
import { FusionAuthProvider, useFusionAuth } from "@fusionauth/react-sdk";
import { AppRouter } from "./AppRouter";
import { Loader } from "./components";

const config = {
  clientID: import.meta.env.VITE_FUSIONAUTH_CLIENT_ID,
  serverUrl: import.meta.env.VITE_TOKEN_EXCHANGE_URL,
  redirectUri: import.meta.env.VITE_TOKEN_EXCHANGE_REDIRECT_URL,

  loginPath: "/auth/login",
  logoutPath: "/auth/logout",
  registerPath: "/auth/register",
  tokenRefreshPath: "/auth/refresh",
  mePath: "/auth/user",
};

const _App_ = () => {
  const { isLoading } = useFusionAuth();
  const [ready, setReady] = useState(false);

  useEffect(() => {
    setTimeout(() => setReady(true), 1500);
  }, [isLoading]);

  return ready ? <AppRouter /> : <Loader />;
};

export const App = () => {
  return (
    <FusionAuthProvider {...config}>
      <_App_ />
    </FusionAuthProvider>
  );
};
