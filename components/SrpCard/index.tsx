"use client";
/* eslint-disable @next/next/no-img-element */
import { useRef } from "react";
import styles from "./SrpCard.module.scss";
import Link from "next/link";

export default function SrpCard({ vehicle }: { vehicle: any }) {
  const imgRef = useRef<HTMLImageElement>(null);
  return (
    <Link
      className={styles.card}
      href={`/vehicle/${vehicle.id}`}
      onClick={() => {
        console.log(imgRef.current?.getBoundingClientRect());
      }}
    >
      <img src={vehicle.image} alt="car" ref={imgRef} />
      <h2>{vehicle.title}</h2>
      <p className={styles.price}>${vehicle.price}</p>
      <p className={styles.vin}>{vehicle.vin}</p>
    </Link>
  );
}
