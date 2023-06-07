"use client";

import { useState, useEffect } from "react";
import SRPCard from "../components/SrpCard";
import styles from "./home.module.scss";

export default function Home() {
  const [vehicles, setVehicles] = useState<{ id: number }[]>([]);

  useEffect(() => {
    async function fetchVehicles() {
      const response = await fetch("http://127.0.0.1:105/vehicles");
      const data = await response.json();
      setVehicles(data);
    }

    fetchVehicles();
  }, []);

  return (
    <div className={styles.main}>
      {vehicles.map((vehicle) => (
        <SRPCard key={vehicle.id} vehicle={vehicle} />
      ))}
    </div>
  );
}
