const getYear = () => new Date().getFullYear();

export const Footer: React.FC = (): JSX.Element => {
  return (
    <footer className="h-[10vh] flex justify-center items-center space-x-5">
      <p>auth-react-client</p>
      <span>{getYear()}</span>
    </footer>
  );
};
