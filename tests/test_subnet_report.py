import unittest

from subnet_report import build_report


class SubnetReportTests(unittest.TestCase):
    def test_normalizes_ipv4_host_to_network(self):
        report = build_report("192.168.10.42/24")

        self.assertEqual(report["network"], "192.168.10.0/24")
        self.assertEqual(report["broadcast_address"], "192.168.10.255")
        self.assertEqual(report["usable_host_count"], 254)
        self.assertEqual(report["first_usable_host"], "192.168.10.1")
        self.assertEqual(report["last_usable_host"], "192.168.10.254")
        self.assertEqual(report["scope"], "privada")

    def test_supports_ipv6(self):
        report = build_report("2001:db8::12/64")

        self.assertEqual(report["version"], 6)
        self.assertEqual(report["network"], "2001:db8::/64")
        self.assertNotIn("broadcast_address", report)

    def test_rejects_invalid_cidr(self):
        with self.assertRaises(ValueError):
            build_report("nao-e-uma-rede")


if __name__ == "__main__":
    unittest.main()
