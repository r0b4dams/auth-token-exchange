import { useEffect, useState } from "react";
import { Navigate, Route, Routes } from "react-router-dom";
import { useFusionAuth } from "@fusionauth/react-sdk";

import { AccountPage, HomePage, MakeChangePage, ProfilePage } from "./pages";
import { Loader, LogoHeader, MenuBar } from "./components";

export const App = () => {
  const { isFetchingUserInfo } = useFusionAuth();
  const [ready, setReady] = useState(false);

  useEffect(() => {
    setTimeout(() => setReady(true), 1500);
  }, [isFetchingUserInfo]);

  if (!ready) {
    return <Loader />;
  }

  return (
    <div id="page-container">
      <div id="page-header">
        <LogoHeader />
        <MenuBar />
      </div>

      <div style={{ flex: 1 }}>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/make-change" element={<MakeChangePage />} />
          <Route path="/account" element={<AccountPage />} />
          <Route path="/profile" element={<ProfilePage />} />
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </div>
    </div>
  );
};
