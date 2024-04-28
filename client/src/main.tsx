import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import {
  FusionAuthProvider,
  FusionAuthProviderConfig,
} from "@fusionauth/react-sdk";

import { App } from "./App.tsx";
import "./index.css";

const config: FusionAuthProviderConfig = {
  clientId: "6e4e9805-9690-476f-a7d8-2552992c41e1",
  redirectUri: "http://localhost:3000",
  serverUrl: "http://localhost:9000",

  loginPath: "/auth/login",
  logoutPath: "/auth/logout",
  registerPath: "/auth/register",
  tokenRefreshPath: "/auth/refresh",
  mePath: "/auth/user",

  shouldAutoFetchUserInfo: true,
  // shouldAutoRefresh: true,
};

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <BrowserRouter>
      <FusionAuthProvider {...config}>
        <App />
      </FusionAuthProvider>
    </BrowserRouter>
  </React.StrictMode>
);
