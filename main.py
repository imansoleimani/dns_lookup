import streamlit as st
from includes import dns_class

domain = st.text_input(label="Domain", placeholder="Please Enter Your Domain...")
additional_dns_servers = st.text_area(label="Additional DNS Servers", placeholder="Please Enter Your DNS Servers (one per line)")

if st.button("Check DNS", type="primary"):

    with st.spinner('Wait for it...'):
        st.text(additional_dns_servers)
        dns_server_additional = additional_dns_servers.splitlines()
        dns_lookup = dns_class.dns_lookup(domain=domain, dns_server_list=dns_server_additional)

        dns_result = dns_lookup.check_dns()
        print(dns_result)
        st.json(dns_result)
        st.success('Done!')
    