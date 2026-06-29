import sys

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if '<!-- Pour Qui Section -->' in line and start_idx == -1:
        start_idx = i
    if '<!-- Conçu pour le Sénégal Section -->' in line:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    new_content = """    <!-- Notre Impact Section -->
    <section id="notre-impact" class="snap-section relative bg-white text-[#111] min-h-screen py-24 flex flex-col justify-center border-t border-[#111]/5 overflow-hidden">
        <!-- Abstract background geometric accents -->
        <div class="absolute top-0 right-0 w-[40rem] h-[40rem] bg-[#111]/[0.02] rounded-full blur-[100px] pointer-events-none"></div>
        <div class="absolute bottom-0 left-0 w-[40rem] h-[40rem] bg-[#111]/[0.02] rounded-full blur-[100px] pointer-events-none"></div>

        <div class="max-w-[88rem] mx-auto px-6 lg:px-12 w-full relative z-10">
            
            <!-- Header -->
            <div class="mb-16 md:mb-24 reveal-item max-w-3xl">
                <span class="text-[11px] font-geist uppercase tracking-[0.3em] text-[#111]/40 block mb-5">// NOTRE IMPACT</span>
                <h2 class="text-3xl md:text-5xl lg:text-6xl font-jakarta font-extralight tracking-tighter leading-[1.1] text-[#111]">
                    Plus qu'une technologie,<br>un levier de développement
                </h2>
            </div>

            <!-- Bento Grid 2x2 -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-px bg-[#111]/10 border border-[#111]/10 relative reveal-item delay-200">
                
                <!-- Card 1 -->
                <div class="bg-white p-10 lg:p-16 flex flex-col hover:bg-[#FAFAFA] transition-colors duration-500 group">
                    <div class="mb-12">
                        <svg viewBox="0 0 100 100" class="w-12 h-12 opacity-40 group-hover:opacity-100 transition-all duration-700 group-hover:-translate-y-2">
                             <ellipse cx="50" cy="30" rx="30" ry="10" fill="none" stroke="#111" stroke-width="1.5"/>
                             <path d="M20 30 v20 A30 10 0 0 0 80 50 v-20" fill="none" stroke="#111" stroke-width="1.5"/>
                             <path d="M20 50 v20 A30 10 0 0 0 80 70 v-20" fill="none" stroke="#111" stroke-width="1.5"/>
                             <path d="M50 30 v40" fill="none" stroke="#111" stroke-width="1.5" stroke-dasharray="2 4"/>
                        </svg>
                    </div>
                    <h3 class="text-[1.35rem] font-jakarta font-medium text-[#111] mb-4">Inclusion financière</h3>
                    <p class="text-[15px] font-manrope font-light text-[#111]/60 leading-relaxed max-w-sm">
                        Les animaux deviennent des actifs reconnus, qui ouvrent crédit et assurance aux éleveurs.
                    </p>
                </div>
                
                <!-- Card 2 -->
                <div class="bg-white p-10 lg:p-16 flex flex-col hover:bg-[#FAFAFA] transition-colors duration-500 group">
                    <div class="mb-12">
                        <svg viewBox="0 0 100 100" class="w-12 h-12 opacity-40 group-hover:opacity-100 transition-all duration-700 group-hover:-translate-y-2">
                             <circle cx="50" cy="50" r="30" fill="none" stroke="#111" stroke-width="1.5" stroke-dasharray="2 4"/>
                             <path d="M50 20 C 80 50, 65 80, 50 80 C 35 80, 20 50, 50 20 Z" fill="none" stroke="#111" stroke-width="1.5"/>
                             <circle cx="50" cy="60" r="4" fill="#111"/>
                        </svg>
                    </div>
                    <h3 class="text-[1.35rem] font-jakarta font-medium text-[#111] mb-4">Souveraineté alimentaire</h3>
                    <p class="text-[15px] font-manrope font-light text-[#111]/60 leading-relaxed max-w-sm">
                        Des produits traçables, du pâturage à l'assiette.
                    </p>
                </div>
                
                <!-- Card 3 -->
                <div class="bg-white p-10 lg:p-16 flex flex-col hover:bg-[#FAFAFA] transition-colors duration-500 group">
                    <div class="mb-12">
                        <svg viewBox="0 0 100 100" class="w-12 h-12 opacity-40 group-hover:opacity-100 transition-all duration-700 group-hover:-translate-y-2">
                            <circle cx="50" cy="25" r="6" fill="none" stroke="#111" stroke-width="1.5"/>
                            <circle cx="25" cy="65" r="6" fill="none" stroke="#111" stroke-width="1.5"/>
                            <circle cx="75" cy="65" r="6" fill="none" stroke="#111" stroke-width="1.5"/>
                            <line x1="45" y1="32" x2="30" y2="58" stroke="#111" stroke-width="1.5" stroke-dasharray="2 4"/>
                            <line x1="55" y1="32" x2="70" y2="58" stroke="#111" stroke-width="1.5" stroke-dasharray="2 4"/>
                            <line x1="32" y1="65" x2="68" y2="65" stroke="#111" stroke-width="1.5"/>
                            <circle cx="50" cy="50" r="2" fill="#111"/>
                        </svg>
                    </div>
                    <h3 class="text-[1.35rem] font-jakarta font-medium text-[#111] mb-4">Inclusion des femmes et des jeunes</h3>
                    <p class="text-[15px] font-manrope font-light text-[#111]/60 leading-relaxed max-w-sm">
                        Dans les chaînes de valeur de l'élevage.
                    </p>
                </div>
                
                <!-- Card 4 -->
                <div class="bg-white p-10 lg:p-16 flex flex-col hover:bg-[#FAFAFA] transition-colors duration-500 group">
                    <div class="mb-12">
                        <svg viewBox="0 0 100 100" class="w-12 h-12 opacity-40 group-hover:opacity-100 transition-all duration-700 group-hover:-translate-y-2">
                            <circle cx="50" cy="50" r="35" fill="none" stroke="#111" stroke-width="1.5"/>
                            <ellipse cx="50" cy="50" rx="35" ry="12" fill="none" stroke="#111" stroke-width="1.5" transform="rotate(90 50 50)"/>
                            <ellipse cx="50" cy="50" rx="35" ry="12" fill="none" stroke="#111" stroke-width="1.5" stroke-dasharray="2 4"/>
                            <path d="M43 43 L57 57 M57 43 L43 57" stroke="#111" stroke-width="1.5"/>
                        </svg>
                    </div>
                    <h3 class="text-[1.35rem] font-jakarta font-medium text-[#111] mb-4">Made in Africa</h3>
                    <p class="text-[15px] font-manrope font-light text-[#111]/60 leading-relaxed max-w-sm">
                        Une solution pensée au Sénégal, pour l'Afrique.
                    </p>
                </div>

            </div>
        </div>
    </section>
"""
    del lines[start_idx:end_idx]
    lines.insert(start_idx, new_content + "\n")
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Successfully replaced.")
else:
    print(f"Tags not found: start_idx={start_idx}, end_idx={end_idx}")
