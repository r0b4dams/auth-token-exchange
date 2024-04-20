import { ButtonHTMLAttributes, PropsWithChildren } from "react";

interface Props
  extends ButtonHTMLAttributes<HTMLButtonElement>,
    PropsWithChildren {}

// thanks to https://flowbite.com/docs/components/buttons/
export const Button: React.FC<Props> = (props) => {
  return (
    <button
      type="button"
      className="text-white bg-blue-700 hover:bg-blue-800 font-medium rounded-lg text-lg px-5 py-2.5 mb-2 w-full"
      {...props}
    >
      {props.children}
    </button>
  );
};
