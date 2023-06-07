/* eslint-disable @next/next/no-img-element */
// "use client";

import vehicles from "@/vehicles";
import styles from "./vehicle.module.scss";

export default function Vehicle({ params }: { params: { id: number } }) {
  const vehicle = vehicles.find((v) => v.id == params.id);

  return (
    <div className={styles.body}>
      <img src={vehicle?.image} alt="car" />
      <h2>{vehicle?.title}</h2>
      <p>${vehicle?.price}</p>
    </div>
  );
}
