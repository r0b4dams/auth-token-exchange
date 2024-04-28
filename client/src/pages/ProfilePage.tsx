import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useFusionAuth } from "@fusionauth/react-sdk";

const imgFallback = "https://cdn-icons-png.flaticon.com/512/149/149071.png";

export const ProfilePage = () => {
  const navigate = useNavigate();
  const { userInfo } = useFusionAuth();
  const isLoggedIn = !!userInfo;

  useEffect(() => {
    if (!isLoggedIn) {
      navigate("/");
    }
  }, [isLoggedIn, navigate]);

  if (!userInfo) {
    return null;
  }

  return (
    <div
      className="app-container"
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
    >
      <img
        alt="avatar"
        src={userInfo.picture || imgFallback}
        style={{ borderRadius: "9999px" }}
        width={200}
        height={200}
      />

      <div
        style={{
          fontSize: 22,
          fontWeight: 700,
          paddingTop: 10,
          paddingBottom: 10,
        }}
      >{`${userInfo.given_name} ${userInfo.family_name}`}</div>
      <div>{userInfo.email}</div>
    </div>
  );
};
