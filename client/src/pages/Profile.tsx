import { Navigate } from "react-router-dom";
import { useFusionAuth } from "@fusionauth/react-sdk";

const imgFallback = "https://cdn-icons-png.flaticon.com/512/149/149071.png";

export const Profile: React.FC = (): JSX.Element => {
  const { user, isAuthenticated } = useFusionAuth();

  if (!isAuthenticated) {
    return <Navigate to="/" />;
  }

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
    >
      <img
        alt="avatar"
        src={user.picture || imgFallback}
        style={{ borderRadius: "9999px" }}
        width={200}
        height={200}
      />

      <div>{`${user.given_name} ${user.family_name}`}</div>
      <div>{user.email}</div>
    </div>
  );
};
