import geni.portal as portal
import geni.rspec.pg as pg

# Create the Portal context
pc = portal.Context()

# Describe the parameter this profile script can accept
pc.defineParameter("n", "Number of Raw machines", portal.ParameterType.INTEGER, 1)

# Retrieve the values the user specifies during instantiation
params = pc.bindParameters()

# Create a Request object to start building the RSpec
rspec = pg.Request()

# Check parameter validity
if params.n < 1 or params.n > 128:
    pc.reportError(portal.ParameterError( "You must choose from 1 to 128"))
    
# Create nodes and links
link = pg.LAN("lan")

disk_image_ubuntu_1204_1 = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU12-64-STD"
disk_image_centos_71_64 = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS71-64-STD"

for i in range (params.n):
    node = pg.RawPC("node"+str(i))
    node.hardware_type = "r320"
    node.disk_image=disk_image_centos_71_64
    bs = node.Blockstore("bs", "/local")
    bs.size = "60GB"

    rspec.addResource(node)
    iface = node.addInterface("if"+str(i))
    link.addInterface(iface)
    node.addService(pg.Install(url="https://github.com/daidong/CloudLab2OpenHPC/archive/master.zip", path="/local"))
    node.addService(pg.Execute(shell="bash", command="/local/install.sh"))

    
rspec.addResource(link)

pc.printRequestRSpec(rspec)