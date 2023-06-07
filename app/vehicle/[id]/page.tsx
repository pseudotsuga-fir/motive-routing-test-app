/* eslint-disable @next/next/no-img-element */
"use client";

import { useState, useEffect } from "react";
import styles from "./vehicle.module.scss";

export default function Vehicle({ params }: { params: { id: number } }) {
  const [vehicle, setVehicle] = useState();

  useEffect(() => {
    console.log(params);
    async function fetchVehicles() {
      const response = await fetch(
        `http://127.0.0.1:105/vehicles/${params.id}`
      );
      const data = await response.json();
      setVehicle(data);
    }

    fetchVehicles();
  }, [params]);
  return (
    <div className={styles.body}>
      <img src={vehicle?.image} alt="car" />
      <h2>{vehicle?.title}</h2>
      <p>${vehicle?.price}</p>
    </div>
  );
}
