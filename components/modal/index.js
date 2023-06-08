"use client";
import { useCallback, useRef, useEffect } from "react";
import { useRouter } from "next/navigation";
import styles from "./modal.module.scss";

export default function Modal({ children }) {
  const router = useRouter();

  const onDismiss = useCallback(() => {
    router.back();
  }, [router]);

  useEffect(() => {
    document.body.style.overflowY = "scroll";
    return () => {
      document.body.style.overflowY = "auto";
    };
  }, []);

  return <div className={styles.overlay}>{children}</div>;
}
