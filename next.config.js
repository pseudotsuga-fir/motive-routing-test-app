/**
 * @type {import('next').NextConfig}
 */
module.exports = {
  reactStrictMode: true,
  images: {
    domains: ["pbs.twimg.com"],
  },
  experimental: {
    scrollRestoration: true,
  },
};
